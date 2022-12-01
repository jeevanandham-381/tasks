//import { AudioOutlined } from '@ant-design/icons';
import React ,{useState}from 'react'
import "antd/dist/antd.css";
import { Button , Space,Input,Menu,Dropdown} from 'antd';
import Link  from 'next/link';
//import {BrowserRouter as Router, Routes, Route,Link}from 'react-router-dom';
export default function Home() {
	const [result, setName] = useState('')

const buttonsty={width:90,marginRight:10,backgroundColor:"skyblue"}

const menu=(
	<Menu
	items={[
		{
			key: '1',
			label: (
			  <a target="_self" rel="admin login" href="http://localhost:3000/adminlogin">
				Admin Login
			  </a>
			),
		  },
		  {
			key: '2',
			label: (
			  <a target="_self" rel="user login" href="http://localhost:3000/Login">
				User Login
			  </a>
			),
		  },
	]}
	/>


)




	return (
	
	<div style={{ display: 'block',
				width: 700, padding: 30,marginLeft:900,backgroundAttachment:"fixed" ,overflow:"hidden"}}>



<body 
      style={{  
   width:600,     
  backgroundImage: "url(" +"https://r2imghtlak.mmtcdn.com/r2-mmt-htl-image/room-imgs/202011191519395848-23820-e7bc2762818611ebab7c0242ac110004.jpg"+ ")",
  backgroundPosition: 'center',
  backgroundSize: 'cover',
  backgroundRepeat: 'no-repeat',
  backgroundAttachment:"fixed"
}}>


</body> 


	<div style={{backgroundAttachment:"fixed",overflow:"hidden"}}>
	<Button Link href='/register' style={buttonsty}>
		Register 
	</Button>
	<Dropdown overlay={menu} placement="bottom">

	<Button Link href='/Login' style={buttonsty}>
		Login
	</Button></Dropdown>
	{/* <Button  href='http://localhost:3000/booking' style={buttonsty}> */}
	<Button Link href='/booking' style={buttonsty}>
		
		Booking
	</Button>

	
<><br/>
<Input style={{marginTop:250,marginRight:20,width:250,color:"black",backgroundColor:"gray",overflow:"hidden"}}
          placeholder="search something" 
          onChange={(e) => setName(e.target.value)}
        /><br/>
      {result }
</>

</div>





	</div>
	
);
}



