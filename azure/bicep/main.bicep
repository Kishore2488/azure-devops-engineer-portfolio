@description('Azure region')
param location string = resourceGroup().location

@description('Environment name')
param environment string

@description('Key Vault name. Must be globally unique.')
param keyVaultName string

resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: keyVaultName
  location: location
  properties: {
    tenantId: subscription().tenantId
    enableRbacAuthorization: true
    sku: {
      family: 'A'
      name: 'standard'
    }
    publicNetworkAccess: 'Enabled'
  }
  tags: {
    environment: environment
    managedBy: 'bicep'
  }
}
