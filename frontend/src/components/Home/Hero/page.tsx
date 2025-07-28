import { useEffect, useState } from "react";

export default function Hero() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/api/hello")
      .then((res) => res.json())
      .then((data) => setMessage(data.message));
  }, []);

  return (
    <div className="h-screen flex items-center justify-center bg-gray-300">
      {message || "Loading..."}
    </div>
  );
}
