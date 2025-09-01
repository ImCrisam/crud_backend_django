from django.core.management.base import BaseCommand
from brands.models import Brand

class Command(BaseCommand):
    help = "Seed initial brands"

    def handle(self, *args, **kwargs):
        brands = [
            ("Nike", "Phil Knight"),
            ("Adidas", "Adolf Dassler"),
            ("Puma", "Rudolf Dassler"),
            ("Reebok", "Joseph Foster"),
            ("Under Armour", "Kevin Plank"),
            ("New Balance", "William Riley"),
            ("Asics", "Kihachiro Onitsuka"),
            ("Fila", "Ettore Fila"),
            ("Converse", "Marquis Mills Converse"),
            ("Vans", "Paul Van Doren"),
            ("Skechers", "Robert Greenberg"),
            ("Columbia", "Paul Lamfrom"),
            ("The North Face", "Douglas Tompkins"),
            ("Patagonia", "Yvon Chouinard"),
            ("Timberland", "Nathan Swartz"),
            ("Levi's", "Levi Strauss"),
            ("Diesel", "Renzo Rosso"),
            ("Lacoste", "René Lacoste"),
            ("Tommy Hilfiger", "Tommy Hilfiger"),
            ("Calvin Klein", "Calvin Klein"),
        ]
        for name, owner in brands:
            Brand.objects.get_or_create(name=name, defaults={"owner": owner})
        self.stdout.write(self.style.SUCCESS("20 brands seeded!"))
