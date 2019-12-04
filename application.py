from flask import Flask, jsonify


app = Flask(__name__)
THUMBPRINT = '698BCD64688E433EAEB3717CB13B011F5D2E573C'


@app.route("/")
def hello():
    with open(f'/var/ssl/certs/{THUMBPRINT}.der') as f:
        content = f.read()
        return jsonify({'der file': content})
    return jsonify({"status": "invite-app running"})


# @app.route("/.well-known/openid-configuration")
# def openid_configuration():
#     issuer = "https://invite-app.azurewebsites.net/"
#     #                 // Sample: Include the absolute URL to JWKs endpoint
#     #                 JwksUri = Url.Link("JWKS", null),
#     #                 // Sample: Include the supported signing algorithms
#     #                 IdTokenSigningAlgValuesSupported = new[] { OidcController.SigningCredentials.Value.Algorithm},
#     #             }), "application/json");
#
#     # with open(f'/var/ssl/certs/{THUMBPRINT}.der') as f:
#     #     pass
#     return jsonify({})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
