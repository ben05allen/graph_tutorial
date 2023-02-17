from msgraph.core import GraphClient
from msgraph.identity import IdentityClient
from msgraph.users import UsersClient

tenant_id = 'your-tenant-id'
client_id = 'your-client-id'
client_secret = 'your-client-secret'

# create authentication client
identity_client = IdentityClient(tenant_id=tenant_id)

# get access token
access_token = identity_client.get_client_credentials_token(client_id, client_secret)

# create graph client
graph_client = GraphClient(access_token=access_token)

# create users client
users_client = UsersClient(graph_client)

# get all user objects and their properties
users = users_client.get_users(properties=['userPrincipalName', 'displayName', 'givenName', 'surname', 'mail'])