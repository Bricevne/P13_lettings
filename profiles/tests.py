import pytest

from django.urls import reverse

from django.contrib.auth.models import User
from profiles.models import Profile


def create_user(username, password):
    """Creates a user for tests."""
    user = User.objects.create(username=username)
    user.set_password(password)
    return user


def create_profile(user, favorite_city):
    """Creates a profile for tests."""
    return Profile.objects.create(user=user, favorite_city=favorite_city)


@pytest.mark.django_db
def test_lettings_index_view(client):
    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 200
    assert b'<title>Profiles</title>' in response.content


@pytest.mark.django_db
def test_letting_view(client):
    user = create_user(username="bricevne", password="AZERTYU")
    profile = create_profile(user=user, favorite_city="Tokyo")
    url = reverse('profiles:profile', kwargs={"username": user.username})
    response = client.get(url)
    assert response.status_code == 200
    assert f'<title>{profile.user.username}</title>'.encode("utf-8") in response.content
