from datetime import timedelta
from urllib import response
from utilities import debug_utils

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate
from django.utils import timezone

from articles.models import Article

def create_user(**kwargs):
    return get_user_model().objects.create(**kwargs)

def create_article(title='article_title', body='article_body', **kwargs):
    return Article.objects.create(title=title, body=body, **kwargs)

# Create your tests here.
class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_list.html')

    def test_no_articles_correct_message(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'No articles yet')
        self.assertQuerysetEqual(response.context['article_list'], [])

    def test_one_article_correct_appearance(self):
        test_user = create_user()
        article = create_article(
            author=test_user, 
            published=True)
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'article_body')
        self.assertQuerysetEqual(response.context['article_list'], [article])

    def test_article_with_future_date(self):
        future_date = timezone.now() + timedelta(days=1)
        user = create_user()
        article = create_article(
            author=user, 
            published=True)
        article.pub_date = future_date
        article.save()
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'No articles yet')
        self.assertQuerysetEqual(response.context['article_list'], [])

    def test_unpublished_article(self):
        user = create_user()
        article = create_article(author=user, published=False)
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'No articles yet')
        self.assertQuerysetEqual(response.context['article_list'], [])


class ArticleDetailPageTests(TestCase):
    def test_article_detail_status_code(self):
        user = create_user()
        article = create_article(published=True, author=user)
        response = self.client.get(reverse('article_detail', kwargs={'pk': article.pk}))
        self.assertEqual(response.status_code, 200)

    def test_unpublished_article_detail_status_code(self):
        user = create_user()
        article = create_article(published=False, author=user)
        response = self.client.get(reverse('article_detail', kwargs={'pk': article.pk}))
        self.assertEqual(response.status_code, 404)

    # def test_paid_article_unpaid_text(self):
    #     user = create_user()
    #     article = create_article(published=False, author=user, is_paid=True)
    #     response = self.client.get(reverse('article_detail', kwargs={'pk': article.pk}))
    #     self.assertEqual(response.status_code, 404)