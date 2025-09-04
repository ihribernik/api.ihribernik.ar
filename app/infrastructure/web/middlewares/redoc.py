def register_redoc(app, spec_url="/swagger.json", route="/redoc", title="API Docs"):
    """
    Inyecta un endpoint Redoc en la app Flask.
    """

    @app.route(route)
    def redoc():
        return f"""
        <!DOCTYPE html>
        <html>
          <head>
            <title>{title}</title>
            <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
          </head>
          <body>
            <redoc spec-url='{spec_url}'></redoc>
          </body>
        </html>
        """
