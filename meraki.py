API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizations()
print(responseb)