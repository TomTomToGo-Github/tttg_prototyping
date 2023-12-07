import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState([{}]);
  const [currentMemberCount, setCurrentMemberCount] = useState([{}]);
  useEffect(() => {
    fetch('/get_members', {method: 'GET', headers: {'Content-Type': 'application/json'}})
      .then(response => response.json())
      .then(
        data => {
          setData(data)
          setCurrentMemberCount(data.list_of_members.length); // Update currentMemberCount
          console.log(data)
          console.log(currentMemberCount)
        } 
      )
    }, [currentMemberCount]);

  const addMember = () => {
    fetch('/add_member', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ new_element: 'new_member' })
    })
      .then(response => response.json())
      .then(data => {
        setData(data);
        setCurrentMemberCount(data.list_of_members.length); // Update currentMemberCount
        console.log(data)
        console.log(currentMemberCount)
      });
  };

  const resetMembers = () => {
    fetch('/reset_members', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.json())
      .then(data => {
        setData(data);
        setCurrentMemberCount(data.list_of_members.length); // Update currentMemberCount
        console.log(data)
        console.log(currentMemberCount)
      });
  };
  

  console.log(data)
  console.log(currentMemberCount)
  return ( 
    <div>
        <button onClick={addMember}>Add Member</button>
        <button onClick={resetMembers}>Reset Member</button>
        {
        (typeof data.list_of_members === 'undefined') ? (<p>loading...</p>) : 
          (
            data.list_of_members.map((member, i) => (
              <p key={i}>{member}</p>
          ))
          )
        }

      </div>
  );

}

export default App;
