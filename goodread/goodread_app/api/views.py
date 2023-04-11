from rest_framework.response import Response
from rest_framework.decorators import api_view
from goodread_app.models import Book
from goodread_app.api.serializers import BookSerializer


@api_view()
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view()
def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)