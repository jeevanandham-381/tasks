import React from 'react'
import "antd/dist/antd.css";
import { Form, Button, Input } from 'antd';
import {  } from 'antd';
import { Select ,Checkbox} from 'antd';
//import styles from'./globals.css'  
//import './demo.css';
export default function Register() {
  const { Option } = Select;

//   const validatePassword = (rule, value, callback) => {
//     if (value && value !== "Secret") {
//       callback("Error!");
//     } else {
//       callback();
    // }

const heading={
	color:"blue"
}

const formbg={
	width:420,
	marginTop:30,
	marginBottom:10,
	backgroundColor:"#D3D3D3"
}
const inputsty={
	width:300,
	marginLeft:-120,
	marginTop:30

}

const formdata={
	marginBottom:"20px" ,marginLeft:"20px"
}



  
	return (
		<div style={{
			display:'block', marginLeft:430,marginRight:500,marginTop:50,justifyContent:'center'
		}}>
			<h1 style={heading} >Create Account</h1>
			{/* <body 
      style={{  
        
  backgroundImage: "url(" +"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWEzLKsjXuIvYo65kJIlROLQFqHnNKuMqrnQ&usqp=CAU"+ ")",
  backgroundPosition: 'center',
  backgroundSize: 'cover',
  backgroundRepeat: 'no-repeat'
}}>
</body>  */}






			{/* <div style={{margin:10,width:400,formbg }} > */}
			<div >
			
			<Form style={formbg}                       //backgroundColor:"#D3D3D3" 
				name="basicform"
				onFinishFailed={(e) => console.log('Failed to submit',e)}
				onFinish={(e) => console.log('Form Submitted',e)}
				initialValues={{ remember: true }}
				action='http://localhost:8000/adduser'  method='post'
			>
        <br/>
			<Form.Item
			label="Enter Your Name"
			name="Name"
			style={formdata}
			rules={[{ required: true,message: 'Please enter username'  }]}
			><Input style={inputsty}/></Form.Item>
      
      <Form.Item
			label="Enter Your Email"
			name="Email"
			style={formdata}
			rules={[{ required: true, message: 'Please enter your email' }]}
			//style={{marginBottom:"20px",marginLeft:"20px"}}
			>
        <Input  style={inputsty}/></Form.Item>

		<Form.Item
			label="Enter Your Phone Number"
			name="number"
			style={formdata}
			rules={[{ required: true, message: 'Please enter your Phone Number' }]}
			//style={{marginBottom:"20px",marginLeft:"20px"}}
			>
        <Input type='number'  min="1" maxLength={10} value="1"
 		 style={{width:300,marginLeft:-175,marginTop:30}}/></Form.Item>
			
      
      <Form.Item
			label="Enter your Gender" name='gender'
			style={formdata}
			rules={[{ required:true, message: 'Please enter your gender' }]}
			>
			

			<Select name="category" placeholder="Please select gender" style={inputsty} >
			{/* style={{width:400,align:'left'}}> */}
			  <Option value="male">Male</Option>
              <Option value="female">Female</Option>
              <Option value="transgender">Transgender</Option>
            </Select>
			</Form.Item>
      
			{/* rules={[{ required: true, message: 'Please enter your gender' }]} */}
			
        {/* <Input  type="text"/> */}
        

			<Form.Item
			label="Enter your Address"
			name="address" 
			style={formdata}

			rules={[{ required: true, message: 'Please enter your address' }]}
			>
        <  Input  style={inputsty} name="address" type="text"/>

			</Form.Item>
      <Form.Item
			
			label="Enter Your Zipcode"
			name="zipcode"
			style={formdata}

			rules={[{ required: true, message: 'Please enter zipcode' }]}
			>
			<Input type="number" style={inputsty}/>

			</Form.Item>

			<Form.Item
			
			label="Enter Your Password"
			name="password"
			style={formdata}
			rules={[{ required: true, message: 'Please enter Password' }]}

			>
			<Input type="password" style={inputsty} pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"/>

			</Form.Item>
      
			
			<br/><br/>
    <div style={{float:"left",width:"300px"}}>
   <Form.Item name="agreement" valuePropName='checked'
   rules={[{ required: true, message: 'read agreement' }]}
   
   
   >

    <Checkbox>I have read the <a href='' >agreement</a></Checkbox>
    
    </Form.Item></div>
			
			{/* <div style={{float:"",width:100 }}><br/><br/> */}
        <Form.Item  style={{}}>
        <Button type="success" htmlType="submit">
			Submit 
			</Button>
			</Form.Item>
			</Form></div>
		</div>
	);
	

	}















	