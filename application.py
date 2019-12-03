from flask import Flask, jsonify

from flask_oidc import OpenIDConnect
app = Flask(__name__)
THUMBPRINT = '698BCD64688E433EAEB3717CB13B011F5D2E573C'
# app.config['OIDC_CLIENT_SECRETS'] = f'/var/ssl/certs/{THUMBPRINT}.der'
# oidc = OpenIDConnect(app)



@app.route("/")
def hello():
    # with open(f'/var/ssl/certs/{THUMBPRINT}.der') as f:
    #     pass
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

    # https://flask-oidc.readthedocs.io/en/latest/
    # with open(f'/var/ssl/certs/{THUMBPRINT}.der') as f:
    #     pass
    return {}


@app.route("/.well-known/keys", name="JWKS")
def keys():
#     # return Content(JsonConvert.SerializeObject(new JwksModel
#     #             {
#     #                 Keys = new[] { JwksKeyModel.FromSigningCredentials(OidcController.SigningCredentials.Value) }
#     #             }), "application/json");
#     pass
    return "/.well-known/keys"


# az webapp config appsettings set --name invite-app --resource-group ringplan --settings WEBSITE_LOAD_CERTIFICATES=*

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)