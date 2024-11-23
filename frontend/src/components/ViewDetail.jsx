import React, { useState } from 'react';
import { FaBed, FaBath, FaWifi, FaCoffee, FaParking, FaTv, FaSnowflake } from 'react-icons/fa';
import image1 from '../assets/image1.jpeg';
import image2 from '../assets/image2.jpeg';
import image3 from '../assets/image3.jpeg';
import image4 from '../assets/image4.jpeg';

const RoomDetailPage = () => {
  const [selectedImage, setSelectedImage] = useState(0);
  
  const room = {
    title: "Executive Suite",
    price: "$250/Night",
    rating: 4,
    images: [
      image1,
      image2,
      image3,
      image4
    ],
    description: "Experience luxury in our spacious Executive Suite, featuring premium amenities and stunning city views. Perfect for business travelers or those seeking extra comfort.",
    features: [
      { icon: <FaBed />, text: "3 King Size Beds" },
      { icon: <FaBath />, text: "2 Bathrooms" },
      { icon: <FaWifi />, text: "High-Speed WiFi" },
      { icon: <FaCoffee />, text: "Mini Kitchen" },
      { icon: <FaParking />, text: "Free Parking" },
      { icon: <FaTv />, text: "55\" Smart TV" },
      { icon: <FaSnowflake />, text: "Climate Control" }
    ],
    details: {
      size: "55 m²",
      maxOccupancy: "4 Adults",
      bedType: "King Size",
      view: "City View"
    },
    policies: [
      
      "No smoking",
      "No pets allowed"
    ]
  };

  const handleBookNow = () => {
    // Handle booking logic here
    console.log('Booking initiated for:', room.title);
  };

  return (
    <div className="container mx-auto py-10 px-16">
      {/* Room Title and Rating */}
      <div className="mb-6 flex justify-between items-start">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">{room.title}</h1>
          <div className="flex items-center mt-2">
            <div className="flex text-[#FF8C00]">
              {"★".repeat(5).split("").map((star, i) => (
                <span key={i} className={i < Math.floor(room.rating) ? "text-[#FF8C00]" : "text-gray-300"}>
                  {star}
                </span>
              ))}
            </div>
            <span className="flex justify-end ml-2 text-gray-600">{room.rating} / 5</span>
          </div>
        </div>
        <div className="text-right">
          <div className="text-2xl font-bold text-[#FF8C00] mb-2">{room.price}</div>
          <a href="/booking">

          <button 
            onClick={handleBookNow}
            className="bg-[#FF8C00] text-white px-8 py-3 rounded-lg font-semibold 
            hover:bg-orange-600 transition transform hover:-translate-y-1"
            >
            Book Now
          </button>
              </a>
        </div>
      </div>

      {/* Image Gallery */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-8">
        <div className="relative h-[400px] bg-gray-100 rounded-lg overflow-hidden">
          <img 
            src={room.images[selectedImage]}
            alt={`Room view ${selectedImage + 1}`}
            className="w-full h-full object-cover"
          />
        </div>
        <div className="grid grid-cols-2 gap-4">
          {room.images.slice(0, 4).map((img, index) => (
            <div 
              key={index}
              className="relative h-[190px] bg-gray-100 rounded-lg overflow-hidden cursor-pointer"
              onClick={() => setSelectedImage(index)}
            >
              <img 
                src={img}
                alt={`Room view ${index + 1}`}
                className="w-full h-full object-cover hover:opacity-90 transition"
              />
            </div>
          ))}
        </div>
      </div>

      {/* Description */}
      <div className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Room Description</h2>
        <p className="text-gray-600 leading-relaxed">
          {room.description}
        </p>
      </div>

      {/* Features */}
      <div className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Room Features</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {room.features.map((feature, index) => (
            <div key={index} className="flex items-center space-x-2 bg-gray-50 p-4 rounded-lg">
              <span className="text-[#FF8C00]">{feature.icon}</span>
              <span className="text-gray-600">{feature.text}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Room Details */}
      <div className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Room Details</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {Object.entries(room.details).map(([key, value]) => (
            <div key={key} className="bg-gray-50 p-4 rounded-lg">
              <div className="text-sm text-gray-500 capitalize">{key}</div>
              <div className="font-semibold">{value}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Policies */}
      <div className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Policies</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {room.policies.map((policy, index) => (
            <div key={index} className="flex items-center space-x-2 bg-gray-50 p-4 rounded-lg">
              <span className="text-gray-600">• {policy}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default RoomDetailPage;