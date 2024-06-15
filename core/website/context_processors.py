from .models import LogoModel

def website_processor(request):
    logo = LogoModel.objects.get(id=1)
    return {"logo_site": logo}
