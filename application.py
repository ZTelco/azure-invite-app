from flask import Flask
# from flask_oidc import OpenIDConnect
app = Flask(__name__)
# oidc = OpenIDConnect(app)

THUMBPRINT = '698BCD64688E433EAEB3717CB13B011F5D2E573C'


@app.route("/")
def hello():
    # with open(f'/var/ssl/certs/{THUMBPRINT}.der') as f:
    #     pass
    return {"status": "invite-app running"}


# @app.route("/.well-known/openid-configuration")
# def keys():
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
    # return {}


# @app.route("/.well-known/keys", name="JWKS")
# def keys2():
#     # return Content(JsonConvert.SerializeObject(new JwksModel
#     #             {
#     #                 Keys = new[] { JwksKeyModel.FromSigningCredentials(OidcController.SigningCredentials.Value) }
#     #             }), "application/json");
#     pass


# az webapp up --sku FREE -n "inviteapp2" -l "Central US"
# az webapp config appsettings set --name invite-app --resource-group ringplan --settings WEBSITE_LOAD_CERTIFICATES=*
