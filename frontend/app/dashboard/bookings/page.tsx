"use client"

import { useState } from "react"
import { TENANTS } from "@/lib/tenant"

export default function BookingsPage() {
  const [selectedTenant, setSelectedTenant] = useState<string>("all")

  const tenantList = Object.entries(TENANTS)

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">🎫 Bookings</h1>
        <p className="text-gray-600">View and manage bookings</p>
      </div>

      {/* Filters */}
      <div className="bg-white rounded-lg shadow p-6 mb-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div>
            <label className="block text-sm font-medium mb-2">🌍 Tenant</label>
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
            <label className="block text-sm font-medium mb-2">📅 Date Range</label>
            <input
              type="date"
              className="w-full p-2 border rounded-lg"
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-2">📋 Status</label>
            <select className="w-full p-2 border rounded-lg">
              <option>All</option>
              <option>Pending</option>
              <option>Confirmed</option>
              <option>Cancelled</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium mb-2">🔍 Search</label>
            <input
              type="text"
              placeholder="Booking ID or customer..."
              className="w-full p-2 border rounded-lg"
            />
          </div>
        </div>
      </div>

      {/* Quick Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-gray-500 text-sm">Total Bookings</h3>
          <p className="text-3xl font-bold">-</p>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-gray-500 text-sm">Pending</h3>
          <p className="text-3xl font-bold text-yellow-500">-</p>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-gray-500 text-sm">Confirmed</h3>
          <p className="text-3xl font-bold text-green-500">-</p>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-gray-500 text-sm">Revenue</h3>
          <p className="text-3xl font-bold">-</p>
        </div>
      </div>

      {/* Bookings Table */}
      <div className="bg-white rounded-lg shadow overflow-hidden">
        <div className="p-4 border-b">
          <span className="text-gray-600">Bookings for: <strong>{selectedTenant === "all" ? "All Tenants" : TENANTS[selectedTenant]?.name}</strong></span>
        </div>
        
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="text-left p-4 font-medium">Booking ID</th>
              <th className="text-left p-4 font-medium">Customer</th>
              <th className="text-left p-4 font-medium">Product</th>
              <th className="text-left p-4 font-medium">Date</th>
              <th className="text-left p-4 font-medium">Status</th>
              <th className="text-left p-4 font-medium">Amount</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-t">
              <td colSpan={6} className="p-8 text-center text-gray-500">
                No bookings yet. Connect to backend API to load bookings.
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      {/* Info Box */}
      <div className="mt-8 bg-blue-50 border border-blue-200 rounded-lg p-4">
        <p className="text-blue-800">
          <strong>💡 Coming soon:</strong> Bookings will be loaded from the Django backend API.
        </p>
      </div>
    </div>
  )
}
