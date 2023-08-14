import React from "react";

const Home = () => {
  return (
    <div className="home-container">
      <h1>Hello!</h1>
      <p>
        My name is JASPA. I am John's automated planning and scheduling
        assistant.
      </p>

      <div className="home-features">
        <h2>Key Features</h2>
        <ul>
          <li>Feature 1: Description of feature 1</li>
          <li>Feature 2: Description of feature 2</li>
          <li>Feature 3: Description of feature 3</li>
          {/* Add more features as needed */}
        </ul>
      </div>

      <div className="home-updates">
        <h2>Recent Updates</h2>
        <ul>
          <li>Update 1: Description of the update</li>
          <li>Update 2: Description of the update</li>
          {/* Add more updates as needed */}
        </ul>
      </div>
    </div>
  );
};

export default Home;
