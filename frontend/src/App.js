import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/example/')
        .then((response) => response.json())
        .then((data) => setData(data))
        .catch((error) => console.error('Error fetching data:', error));
}, []);


  return (
    <div className="App">
      <h1>Finance Buddy</h1>
      {data ? (
        <div>
          <p>Message: {data.message}</p>
          <p>Status: {data.status}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;
