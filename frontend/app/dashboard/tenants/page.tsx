import { TENANTS } from "@/lib/tenant"
import Link from "next/link"

export default function TenantsPage() {
  const tenantList = Object.entries(TENANTS)

  return (
    <div>
      <div className="mb-8 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold mb-2">🏢 Tenants</h1>
          <p className="text-gray-600">Manage all {tenantList.length} tenants</p>
        </div>
      </div>

      {/* Tenants Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {tenantList.map(([key, tenant]) => (
          <div key={key} className="bg-white rounded-lg shadow overflow-hidden">
            {/* Hero Image Preview */}
            <div 
              className="h-32 bg-cover bg-center"
              style={{ backgroundImage: `url(${tenant.heroImage})` }}
            />
            
            {/* Tenant Info */}
            <div className="p-4">
              <h3 className="text-xl font-bold mb-1">{tenant.name}</h3>
              <p className="text-sm text-gray-500 mb-3">Key: {key}</p>
              <p className="text-gray-600 text-sm line-clamp-2 mb-4">
                {tenant.heroTitle}
              </p>
              
              <Link 
                href={`/dashboard/tenants/${key}`}
                className="block w-full text-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
              >
                Edit Tenant
              </Link>
            </div>
          </div>
        ))}
      </div>

      {/* Summary */}
      <div className="mt-8 bg-white rounded-lg shadow p-6">
        <h2 className="text-lg font-bold mb-4">Tenant Summary</h2>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
          {tenantList.map(([key, tenant]) => (
            <div key={key} className="text-center p-3 border rounded-lg">
              <div className="font-medium">{tenant.name}</div>
              <div className="text-xs text-gray-500">{key}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
