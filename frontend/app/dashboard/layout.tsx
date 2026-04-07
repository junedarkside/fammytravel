import Link from 'next/link'

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="flex min-h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-gray-900 text-white p-4">
        <div className="mb-8">
          <h1 className="text-xl font-bold">🏝️ Fammytravel</h1>
          <p className="text-sm text-gray-400">Admin Dashboard</p>
        </div>
        
        <nav className="space-y-2">
          <Link href="/dashboard" className="block p-2 rounded hover:bg-gray-800">
            📊 Overview
          </Link>
          <Link href="/dashboard/tenants" className="block p-2 rounded hover:bg-gray-800">
            🏢 Tenants
          </Link>
          <Link href="/dashboard/products" className="block p-2 rounded hover:bg-gray-800">
            📦 Products
          </Link>
          <Link href="/dashboard/bookings" className="block p-2 rounded hover:bg-gray-800">
            🎫 Bookings
          </Link>
        </nav>
        
        <div className="mt-8 pt-4 border-t border-gray-700">
          <Link href="/" className="block p-2 text-sm text-gray-400 hover:text-white">
            ← Back to Site
          </Link>
        </div>
      </aside>
      
      {/* Main Content */}
      <main className="flex-1 p-8">
        {children}
      </main>
    </div>
  )
}
