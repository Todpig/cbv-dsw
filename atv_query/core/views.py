from django.shortcuts import render
from .models import Book, Author, Tag, Review
from django.db.models import Count, Q

def query_examples(request):
    # Consulta simples com filter
    books_by_title = Book.objects.filter(title__icontains='teste')

    # Consulta com lookup para buscar autores por nome
    authors_by_name = Author.objects.filter(name__icontains='nome do autor')

    # Consulta many-to-many (livros com uma determinada tag)
    books_with_tag = Book.objects.filter(tags__name='nome da tag')

    # Consulta para encontrar autores com biografias que contêm uma palavra ou frase específica
    authors_with_biography_keyword = Author.objects.filter(biography__icontains='palavra ou frase específica')

    # Consulta com relacionamento reverso (todos os livros de um autor)
    books_of_author = Book.objects.filter(author__name='nome do autor')

    # Consulta agregada (por exemplo, número de livros de um autor)
    num_books_of_author = Book.objects.filter(author__name='nome do autor').count()

    # Consulta para encontrar livros com pelo menos uma avaliação com classificação igual ou superior a 4
    books_with_high_ratings = Book.objects.filter(review__rating__gte=4)

    # Consulta para encontrar perfis de usuários com um website específico
    user_profiles_with_website = Profile.objects.filter(website='http://www.exemplo.com')

    # Consulta para encontrar livros sem avaliações
    books_without_reviews = Book.objects.exclude(reviews__isnull=False)

    # Consulta para listar autores com base no número de livros, ordenando do maior para o menor
    authors_with_most_books = Author.objects.annotate(num_books=Count('books')).order_by('-num_books')

    # Consulta para encontrar livros com resumos mais longos que 150 palavras
    books_with_long_summaries = Book.objects.filter(
    summary__isnull=False,  
    summary__words__gt=150 
    )

    # Consulta para encontrar todas as avaliações dos livros do autor específico
    autor_especifico = Author.objects.get(name='Nome do Autor')
    avaliacoes_do_autor = Review.objects.filter(book__author=autor_especifico)

    tags_especificas = ['Poesia', 'Ciência']
    livros_com_tags_especificas = Book.objects.filter(
    tags__name__in=tags_especificas
).distinct().annotate(num_tags=Count('tags')).filter(num_tags=len(tags_especificas))

    context = {
        'books_by_title': books_by_title,
        'authors_by_name': authors_by_name,
        'books_with_tag': books_with_tag,
        'books_of_author': books_of_author,
        'num_books_of_author': num_books_of_author,
        "authors_with_biography_keyword": authors_with_biography_keyword,
        "books_with_high_ratings": books_with_high_ratings,
        "user_profiles_with_website": user_profiles_with_website,
        "books_without_reviews": books_without_reviews,
        "authors_with_most_books": authors_with_most_books,
        "avaliacoes_do_autor": avaliacoes_do_autor,
        "livros_com_tags_especificas": livros_com_tags_especificas,
    }

    return render(request, 'core/teste1.html', context)
