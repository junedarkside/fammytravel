"use client"

import { useState } from "react"
import { TENANTS } from "@/lib/tenant"

export default function ProductsPage() {
  const [selectedTenant, setSelectedTenant] = useState<string>("all")

  const tenantList = Object.entries(TENANTS)

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">📦 Products</h1>
        <p className="text-gray-600">Manage products across all tenants</p>
      </div>

      {/* Filters */}
      <div className="bg-white rounded-lg shadow p-6 mb-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label className="block text-sm font-medium mb-2">🌍 Filter by Tenant</label>
            <select
              value={selectedTenant}
              onChange={(e) => setSelectedTenant(e.target.value)}
              className="w-full p-2 border rounded-lg"
            >
              <option value="all">All Tenants</option>
              {tenantList.map(([key, tenant]) => (
                <option key={key} value={key}>
                  {tenant.name}
                </option>
              ))}
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium mb-2">🔍 Search</label>
            <input
              type="text"
              placeholder="Search products..."
              className="w-full p-2 border rounded-lg"
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-2">📋 Status</label>
            <select className="w-full p-2 border rounded-lg">
              <option>All Status</option>
              <option>Active</option>
              <option>Inactive</option>
            </select>
          </div>
        </div>
      </div>

      {/* Products Table */}
      <div className="bg-white rounded-lg shadow overflow-hidden">
        <div className="p-4 border-b flex justify-between items-center">
          <span className="text-gray-600">Showing products for: <strong>{selectedTenant === "all" ? "All Tenants" : TENANTS[selectedTenant]?.name}</strong></span>
          <button className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
            + Add Product
          </button>
        </div>
        
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="text-left p-4 font-medium">Product</th>
              <th className="text-left p-4 font-medium">Tenant</th>
              <th className="text-left p-4 font-medium">Price</th>
              <th className="text-left p-4 font-medium">Status</th>
              <th className="text-left p-4 font-medium">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-t">
              <td colSpan={5} className="p-8 text-center text-gray-500">
                No products yet. Connect to backend API to load products.
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      {/* Info Box */}
      <div className="mt-8 bg-blue-50 border border-blue-200 rounded-lg p-4">
        <p className="text-blue-800">
          <strong>💡 Coming soon:</strong> Products will be loaded from the Django backend API.
          Configure the API endpoint in <code>frontend/.env.local</code>
        </p>
      </div>
    </div>
  )
}
