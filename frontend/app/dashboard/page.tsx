"use client"

import { useState } from "react"
import { TENANTS } from "@/lib/tenant"
import Link from "next/link"

export default function DashboardPage() {
  const [selectedTenant, setSelectedTenant] = useState<string>("all")

  const tenantList = Object.entries(TENANTS)

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">Dashboard Overview</h1>
        <p className="text-gray-600">Manage your tenants and products</p>
      </div>

      {/* Tenant Selector */}
      <div className="bg-white rounded-lg shadow p-6 mb-8">
        <label className="block text-sm font-medium mb-2">🌍 Select Tenant</label>
        <select
          value={selectedTenant}
          onChange={(e) => setSelectedTenant(e.target.value)}
          className="w-full max-w-xs p-2 border rounded-lg"
        >
          <option value="all">All Tenants</option>
          {tenantList.map(([key, tenant]) => (
            <option key={key} value={key}>
              {tenant.name}
            </option>
          ))}
        </select>
      </div>

      {/* Quick Stats */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-gray-500 text-sm">Total Tenants</h3>
          <p className="text-3xl font-bold">{tenantList.length}</p>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-gray-500 text-sm">Products</h3>
          <p className="text-3xl font-bold">-</p>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-gray-500 text-sm">Bookings</h3>
          <p className="text-3xl font-bold">-</p>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-bold mb-4">Quick Actions</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <Link 
            href="/dashboard/tenants"
            className="p-4 border rounded-lg hover:bg-gray-50 text-center"
          >
            <div className="text-2xl mb-2">🏢</div>
            <div className="font-medium">Manage Tenants</div>
          </Link>
          <Link 
            href="/dashboard/products"
            className="p-4 border rounded-lg hover:bg-gray-50 text-center"
          >
            <div className="text-2xl mb-2">📦</div>
            <div className="font-medium">Manage Products</div>
          </Link>
          <Link 
            href="/dashboard/bookings"
            className="p-4 border rounded-lg hover:bg-gray-50 text-center"
          >
            <div className="text-2xl mb-2">🎫</div>
            <div className="font-medium">View Bookings</div>
          </Link>
        </div>
      </div>

      {/* Tenant Preview */}
      {selectedTenant !== "all" && TENANTS[selectedTenant] && (
        <div className="bg-white rounded-lg shadow p-6 mt-8">
          <h2 className="text-xl font-bold mb-4">Selected Tenant Preview</h2>
          <div className="bg-gray-50 rounded-lg p-4">
            <p className="font-medium">{TENANTS[selectedTenant].name}</p>
            <p className="text-gray-600 mt-1">{TENANTS[selectedTenant].heroTitle}</p>
            <p className="text-sm text-gray-500 mt-2">{TENANTS[selectedTenant].heroSubtitle}</p>
          </div>
          <Link 
            href={`/dashboard/tenants/${selectedTenant}`}
            className="inline-block mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            Edit Tenant
          </Link>
        </div>
      )}
    </div>
  )
}
