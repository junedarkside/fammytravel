"use client"

import { useState } from "react"
import Link from "next/link"
import { useParams } from "next/navigation"
import { TENANTS } from "@/lib/tenant"

export default function TenantEditPage() {
  const params = useParams()
  const tenantId = params.id as string
  
  const tenant = TENANTS[tenantId]
  const [formData, setFormData] = useState({
    name: tenant?.name || "",
    heroTitle: tenant?.heroTitle || "",
    heroSubtitle: tenant?.heroSubtitle || "",
    heroImage: tenant?.heroImage || "",
  })

  if (!tenant) {
    return (
      <div>
        <h1 className="text-3xl font-bold">Tenant not found</h1>
        <p className="text-gray-600 mt-2">Tenant "{tenantId}" does not exist.</p>
        <Link href="/dashboard/tenants" className="text-blue-600 hover:underline mt-4 block">
          ← Back to Tenants
        </Link>
      </div>
    )
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // TODO: Connect to backend API
    alert(`Saving ${tenantId}: ${formData.name}`)
  }

  return (
    <div>
      <div className="mb-8">
        <Link href="/dashboard/tenants" className="text-blue-600 hover:underline mb-4 block">
          ← Back to Tenants
        </Link>
        <h1 className="text-3xl font-bold">✏️ Edit Tenant: {tenant.name}</h1>
        <p className="text-gray-600">Tenant ID: {tenantId}</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Edit Form */}
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-xl font-bold mb-6">Tenant Settings</h2>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">Tenant Name</label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                className="w-full p-2 border rounded-lg"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Hero Title</label>
              <input
                type="text"
                name="heroTitle"
                value={formData.heroTitle}
                onChange={handleChange}
                className="w-full p-2 border rounded-lg"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Hero Subtitle</label>
              <textarea
                name="heroSubtitle"
                value={formData.heroSubtitle}
                onChange={handleChange}
                rows={2}
                className="w-full p-2 border rounded-lg"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Hero Image URL</label>
              <input
                type="text"
                name="heroImage"
                value={formData.heroImage}
                onChange={handleChange}
                className="w-full p-2 border rounded-lg"
              />
            </div>
            <button
              type="submit"
              className="w-full py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
            >
              Save Changes
            </button>
          </form>
        </div>

        {/* Live Preview */}
        <div>
          <h2 className="text-xl font-bold mb-4">Live Preview</h2>
          <div className="bg-white rounded-lg shadow overflow-hidden">
            <div 
              className="h-48 bg-cover bg-center"
              style={{ backgroundImage: `url(${formData.heroImage})` }}
            />
            <div className="p-6">
              <h3 className="text-2xl font-bold mb-2">{formData.name}</h3>
              <p className="text-lg text-gray-800 mb-2">{formData.heroTitle}</p>
              <p className="text-gray-600">{formData.heroSubtitle}</p>
            </div>
          </div>
          
          <div className="mt-4 p-4 bg-gray-100 rounded-lg">
            <p className="text-sm text-gray-600">
              <strong>URL:</strong> <code>/{tenantId}</code> or <code>/{tenantId === 'main' ? '' : tenantId}.fammytravel.com</code>
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
