import { useState } from "react";


export default function simpleArray(){
    const[users,setUser]=useState([
        {
        id:1,
        name:"rajkumar",
        type:"admin"
        },
        {
            id:2,
            name:"demo",
            type:"user"
            }
    ]);
    
    // export default function simpleArray(){

    return(
<div>
    <ul>
        {users.map((user)=>(<div key={user.id}>
            <p>id:      {user.id}</p>
            <p> Name:   {user.name}</p>
            <p>Role:     {user.type}</p>
          </div>
        ))}
    </ul>
</div>





        
    );
        }
        
    

    
