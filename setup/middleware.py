from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Permitir acesso ao login, logout, admin e arquivos estáticos
        if request.path.startswith('/login') or request.path.startswith('/logout') or request.path.startswith('/admin') or request.path.startswith('/static'):
            return self.get_response(request)

        # Se não estiver logado, redireciona
        if not request.session.get('funcionario_id'):
            return redirect('login')

        return self.get_response(request)
