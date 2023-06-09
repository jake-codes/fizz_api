def register_routes(api, app, root="api"):
    from app.widget import register_routes as attach_widget
    from app.fizz import register_routes as attach_fizz
    from app.generatetraffic import register_routes as attach_generatetraffic
    from app.third_party.app import create_bp

    # Add routes
    attach_widget(api, app)
    attach_fizz(api, app)
    attach_generatetraffic(api, app)
    app.register_blueprint(create_bp(), url_prefix="/third_party")
