# 1. Resource Group
resource "azurerm_resource_group" "rg" {
  name     = "rg-${var.student_name}-final"
  location = var.location
  tags = {
    Project     = "Final"
    StudentName = var.student_name
  }
}

# 2. Azure Container Registry (ACR) - Basic SKU
resource "azurerm_container_registry" "acr" {
  name                = "acryousefomarmohammedfinal" # <-- HARDCODED: No spaces, no hyphens, all lowercase
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = false
  tags = {
    Project     = "Final"
    StudentName = var.student_name
  }
}

# 3. Azure Kubernetes Service (AKS) - 2 nodes, Standard_B2s
resource "azurerm_kubernetes_cluster" "aks" {
  name                = "acr${replace(lower(var.student_name), "-", "")}final"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "aks-${var.student_name}"

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_D2s_v3"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Project     = "Final"
    StudentName = var.student_name
  }
}

# 4. AKS + ACR Integration (Automatic image pull)
resource "azurerm_role_assignment" "aks_acr_pull" {
  principal_id                     = azurerm_kubernetes_cluster.aks.kubelet_identity[0].object_id
  role_definition_name             = "AcrPull"
  scope                            = azurerm_container_registry.acr.id
  skip_service_principal_aad_check = true
}