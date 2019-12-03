from flask import Flask, jsonify


app = Flask(__name__)
THUMBPRINT = '698BCD64688E433EAEB3717CB13B011F5D2E573C'


@app.route("/")
def hello():
    with open(f'/var/ssl/certs/{THUMBPRINT}.der') as f:
        content = f.read()
        return jsonify({'der file': content})
    return jsonify({"status": "invite-app running"})


@app.route("/.well-known/openid-configuration")
def openid_configuration():
    # return Content(JsonConvert.SerializeObject(new OidcModel
    #             {
    #                 // Sample: The issuer name is the application root path
    #                 Issuer = $"{this.Request.Scheme}://{this.Request.Host}{this.Request.PathBase.Value}/",
    issuer = "https://invite-app.azurewebsites.net/"
    #
    #                 // Sample: Include the absolute URL to JWKs endpoint
    #                 JwksUri = Url.Link("JWKS", null),

    #
    #                 // Sample: Include the supported signing algorithms
    #                 IdTokenSigningAlgValuesSupported = new[] { OidcController.SigningCredentials.Value.Algorithm},
    #             }), "application/json");

    # with open(f'/var/ssl/certs/{THUMBPRINT}.der') as f:
    #     pass
    return jsonify({
        "issuer": "https://example.com/",
        "authorization_endpoint": "https://example.com/authorize",
        "token_endpoint": "https://example.com/token",
        "userinfo_endpoint": "https://example.com/userinfo",
        "jwks_uri": "https://example.com/.well-known/jwks.json",
        "scopes_supported": [
            "pets_read",
            "pets_write",
            "admin"
        ],
        "response_types_supported": [
            "code",
            "id_token",
            "token id_token"
        ],
        "token_endpoint_auth_methods_supported": [
            "client_secret_basic"
        ],
    })


@app.route("/.well-known/keys")
def keys():
#     # return Content(JsonConvert.SerializeObject(new JwksModel
#     #             {
#     #                 Keys = new[] { JwksKeyModel.FromSigningCredentials(OidcController.SigningCredentials.Value) }
#     #             }), "application/json");
#     pass
    return "/.well-known/keys"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)