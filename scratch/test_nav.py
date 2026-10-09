from app import app

client = app.test_client()

routes = [
    '/',
    '/subjects',
    '/progress',
    '/resources',
    '/study-plan',
    '/login',
    '/register'
]

for route in routes:
    res = client.get(route)
    assert res.status_code == 200, f"Failed on {route}: {res.status_code}"
    html = res.data.decode('utf-8')
    assert 'class="navbar"' in html, f"Navbar missing in {route}"
    assert 'class="nav-links"' in html, f"Nav links missing in {route}"
    assert 'class="nav-dropdown"' in html, f"Dropdown missing in {route}"
    assert 'How It Works' in html, f"How It Works missing in {route}"
    assert 'About SDG 4' in html, f"About SDG 4 missing in {route}"
    assert 'mobileDrawer' in html, f"Mobile drawer missing in {route}"
    print(f"✓ Route {route} rendered navbar successfully")

print("ALL NAVBAR TESTS PASSED!")
