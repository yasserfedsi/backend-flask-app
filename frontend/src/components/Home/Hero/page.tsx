import axios from "axios";
import { useEffect, useState } from "react";
import { API_BASE_URL } from "../../../callback/api";

export default function Hero() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    async function fetchMessage() {
      try {
        const response = await axios.get(`${API_BASE_URL}` + "api/hello");
        setMessage(response.data.message);
      } catch (error) {
        console.error("Error fetching message:", error);
        setMessage("Failed to load message");
      }
    }

    fetchMessage();
  }, []);

  return (
    <div className="h-screen flex items-center justify-center bg-white">
      <div className="p-6 h-auto w-auto border border-gray-400 rounded-lg shadow-lg">
        {message || "Loading..."}
      </div>
    </div>
  );
}
