BASE_ROUTE = "traffic"


def register_routes(api, app, root="api"):
    from .controller import api as traffic_api

    api.add_namespace(traffic_api, path=f"/{root}/{BASE_ROUTE}")