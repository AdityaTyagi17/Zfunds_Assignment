from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Product, ProductCategory


@api_view(['POST'])
def advisor_signup(request):
    try:   
        name = request.data.get('name')
        mobile = request.data.get('mobile')
        if not mobile:
            return Response({'error': 'Mobile number is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the advisor account
        advisor = User.objects.create(name=name, mobile=mobile, role="advisor")

        return Response({'message': 'Advisor account created successfully.'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_client(request):
    try:
        advisor_id = request.data.get('advisor_id')
        client_name = request.data.get('client_name')
        client_mobile = request.data.get('client_mobile')

        if not advisor_id or not client_name or not client_mobile:
            return Response({'error': 'Advisor ID, client name, and client mobile are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the advisor exists
        advisor = User.objects.filter(id=advisor_id, role='advisor').first()
        if not advisor:
            return Response({'error': 'Advisor not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if a user with the same mobile number already exists
        client = User.objects.filter(mobile=client_mobile, role='user').first()
        if client:
            # If the client already exists, update its advisor
            client.advisor = advisor
            client.save()
            return Response({'message': f'Client {client_name} updated with advisor {advisor.name}.'},
                            status=status.HTTP_200_OK)
        else:
            # Create the client account and associate it with the advisor
            client = User.objects.create(name=client_name, mobile=client_mobile, role='user', advisor=advisor)
            return Response({'message': f'Client {client_name} added to advisor {advisor.name} successfully.'},
                            status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def list_clients(request, advisor_id):
    try:
        clients = User.objects.filter(advisor_id=advisor_id, role='user')

        client_list = [{'name': client.name, 'mobile': client.mobile} for client in clients]

        return Response(client_list, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'Advisor not found or no clients linked to this advisor.'},
                        status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def user_signup(request):
    try:
        user_name = request.data.get('user_name')
        user_mobile = request.data.get('user_mobile')
        user_role = 'user' 

        if not user_name or not user_mobile:
            return Response({'error': 'User name and mobile number are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(mobile=user_mobile).exists():
            return Response({'error': 'A user with this mobile number already exists.'},
                            status=status.HTTP_409_CONFLICT)

        # Create the user account
        user = User.objects.create(name=user_name, mobile=user_mobile, role=user_role)

        return Response({'message': 'User account created successfully.'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_product(request):
    try:
        product_name = request.data.get('product_name')
        description = request.data.get('description')
        category = request.data.get('category')

        if not product_name or not description or not category:
            return Response({'error': 'Product name, description, and category are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        existing_category = Product.objects.filter(category=category).first()
        if not existing_category:
            new_category = ProductCategory.objects.create(name=category)
            category = new_category.name

        # Create the product
        product = Product.objects.create(name=product_name, description=description, category=category)

        return Response({'message': 'Product added successfully.', 'product_id': product.id,'product_name': product.name,'category': product.category},
                        status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def purchase_product(request, advisor_id, user_id):
    try:
        product_id = request.data.get('product_id')

        if not product_id:
            return Response({'error': 'Product ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the advisor exists
        advisor = User.objects.filter(id=advisor_id, role='advisor').first()
        if not advisor:
            return Response({'error': 'Advisor not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the client exists and is managed by the advisor
        user = User.objects.filter(id=user_id, role='user', advisor=advisor).first()
        if not user:
            return Response({'error': 'User not found or not managed by this advisor.'},
                            status=status.HTTP_404_NOT_FOUND)

        # Check if the product exists
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        user.products=product.name
        user.save()
        return Response({
                            'message': f'Product {product.name} associated with user {user.name} by advisor {advisor.name} successfully.', 'ProductLink=':f'https://producturl/{product.id}'},
                        status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
