import pytest

from django.urls import reverse

from lettings.models import Address, Letting


def create_address(number, street, city, state, zip_code, country_iso_code):
    """Creates an address for tests."""
    return Address.objects.create(
        number=number,
        street=street,
        city=city,
        state=state,
        zip_code=zip_code,
        country_iso_code=country_iso_code
    )


def create_letting(title, address):
    """Creates a letting for tests."""
    return Letting.objects.create(title=title, address=address)


@pytest.mark.django_db
def test_lettings_index_view(client):
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assert b'<title>Lettings</title>' in response.content


@pytest.mark.django_db
def test_letting_view(client):
    address = create_address(
        number=197,
        street="Impasse Germaine Tillion",
        city="Périgueux",
        state="Dordogne",
        zip_code=24750,
        country_iso_code="3166-2:FR"
    )
    letting = create_letting(
        title="New title",
        address=address
    )
    url = reverse('lettings:letting', kwargs={"letting_id": letting.id})
    response = client.get(url)
    assert response.status_code == 200
    assert f'<title>{letting.title}</title>'.encode("utf-8") in response.content
