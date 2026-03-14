import Link from 'next/link';
import { MapPin, Plane, Mountain, Calendar } from 'lucide-react';

export default function Home() {
  return (
    <main className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[500px] flex items-center justify-center bg-gradient-to-br from-primary-600 to-primary-800">
        <div className="absolute inset-0 bg-black/30" />
        <div className="relative z-10 text-center text-white px-4">
          <h1 className="text-5xl font-bold mb-4">Fammytravel</h1>
          <p className="text-xl mb-8">Discover Amazing Destinations</p>
          <p className="text-primary-100">Your Trusted Travel Partner for Switzerland & Beyond</p>
        </div>
      </section>

      {/* Features */}
      <section className="py-16 px-4 max-w-6xl mx-auto">
        <h2 className="text-3xl font-bold text-center mb-12">Why Choose Us</h2>
        <div className="grid md:grid-cols-3 gap-8">
          <div className="text-center p-6 bg-white rounded-lg shadow-md">
            <MapPin className="w-12 h-12 mx-auto mb-4 text-primary-600" />
            <h3 className="text-xl font-semibold mb-2">Curated Destinations</h3>
            <p className="text-gray-600">Handpicked places for unforgettable experiences</p>
          </div>
          <div className="text-center p-6 bg-white rounded-lg shadow-md">
            <Plane className="w-12 h-12 mx-auto mb-4 text-primary-600" />
            <h3 className="text-xl font-semibold mb-2">Easy Booking</h3>
            <p className="text-gray-600">Simple and secure reservation process</p>
          </div>
          <div className="text-center p-6 bg-white rounded-lg shadow-md">
            <Mountain className="w-12 h-12 mx-auto mb-4 text-primary-600" />
            <h3 className="text-xl font-semibold mb-2">Local Experts</h3>
            <p className="text-gray-600">Knowledgeable guides for authentic experiences</p>
          </div>
        </div>
      </section>

      {/* Destinations */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">Popular Destinations</h2>
          <div className="grid md:grid-cols-2 gap-8">
            <div className="bg-white rounded-lg overflow-hidden shadow-md">
              <div className="h-48 bg-primary-200 flex items-center justify-center">
                <Mountain className="w-16 h-16 text-primary-600" />
              </div>
              <div className="p-6">
                <h3 className="text-xl font-semibold mb-2">Switzerland</h3>
                <p className="text-gray-600 mb-4">Experience the beauty of the Alps</p>
                <Link 
                  href="/destinations/switzerland"
                  className="text-primary-600 font-semibold hover:text-primary-700"
                >
                  Explore →
                </Link>
              </div>
            </div>
            <div className="bg-white rounded-lg overflow-hidden shadow-md">
              <div className="h-48 bg-primary-200 flex items-center justify-center">
                <Plane className="w-16 h-16 text-primary-600" />
              </div>
              <div className="p-6">
                <h3 className="text-xl font-semibold mb-2">Japan</h3>
                <p className="text-gray-600 mb-4">Discover tradition and modernity</p>
                <Link 
                  href="/destinations/japan"
                  className="text-primary-600 font-semibold hover:text-primary-700"
                >
                  Explore →
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8">
        <div className="max-w-6xl mx-auto px-4 text-center">
          <p>© 2026 Fammytravel. All rights reserved.</p>
        </div>
      </footer>
    </main>
  );
}
