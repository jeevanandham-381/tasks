import React, { useContext } from 'react'
import "./../node_modules/antd/dist/antd.css";
import { withAuthenticator } from '@aws-amplify/ui-react';
//import Amplify from 'aws-amplify';
import './../awsconfiguration'
import { Form, Button, Input, Layout  } from 'antd';
//import Link from 'next/link';
import { Content } from './../node_modules/antd/lib/layout/layout';
import { useFormik } from 'formik';
import Password from 'antd/lib/input/Password';
//import { ComponentClassName } from '@aws-amplify/ui-react/dist/types/primitives/shared/types';

// const layout = {
//     labelCol: { xs: { span: 24 }, sm: { span: 12 }, md: { span: 8 }, lg: { span: 8 } },
//     wrapperCol: { xs: { span: 24 }, sm: { span: 12 }, md: { span: 12 }, lg: { span: 12 } }
// }
// const tailLayout = {
//     wrapperCol: { xs: { span: 24 }, sm: { span: 12, offset: 12 }, md: { span: 12, offset: 8 }, lg: { span: 12, offset: 8 } }
// }

function Login(props){
// 	const{switchToSignin}=useContext(AccountContext);

// 	const onSubmit=(values)=>{
// 		alert(JSON.stringify(value));
// 	};
// 	const formik=useFormik({initialValues:{Username:"",password:""},
//      validateonBlur:true,
// 	 onSubmit,
// })
	



	return (
		<div style={{
			display:'block', marginLeft:400,marginRight:400,marginTop:50,justifyContent:'center',
		}}>
			
            {/* <body style={{backgroundColor:'pink'}}></body> */}
                
			<h1 >Login Page</h1>

            {/* <body 
      style={{  
        
  backgroundImage: "url(" +"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWEzLKsjXuIvYo65kJIlROLQFqHnNKuMqrnQ&usqp=CAU"+ ")",
  backgroundPosition: 'center',
  backgroundSize: 'cover',
  backgroundRepeat: 'no-repeat'
}}>
</body>  */}
{/* .centered{{
    backgroundPosition: 'center',
    backgroundSize:'50%'
}} */}


            <Layout ><Content >  
            <div style={{margin:10,width:450,padding:50}} >
			<Form 
				name="basicform"
				onFinishFailed={(e) => console.log('Failed to login',e)}
				onFinish={() => alert('successfully loggedin')}
				// initialValues={{ remember: true }}
			>
			<Form.Item 
			label="Enter username"
			name="Username"
			// value={formik.value.Username} onchannge={formik.handleChange}
            style={{marginBottom:"0px"}}
			rules={[{ required: true, message: 'Please enter username' }]}
			><Input  />
		   </Form.Item><br/><br/>
		   <Form.Item 
			label="Enter password"
			name="password" type='password'
			// value={formik.value.Username} onchannge={formik.handleChange}
            style={{marginBottom:"0px"}}    
						rules={[{ required: true, message: 'Please enter username' }]}
			><Input.Password/>
		   </Form.Item>
		   
           {/* <Form.Item 
			label="Enter Password"
			name="Userpass"
            style={{marginBottom:"0px"}}
			rules={[{ required: true, message: 'Please enter valid password' ,pattern:"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"}]}
			><Input />
		   </Form.Item><br/><br/> */}
			<Form.Item>
			<Button type="success" htmlType="submit" className='click' style={{color:"blue",marginTop:"20px" }}>
			Submit 
			</Button>
			<Button href='http://localhost:3000/home' style={{width:90,marginLeft:30,color:"red"}}>
		Back 
	</Button>
	
			</Form.Item>
			</Form></div></Content></Layout>
		</div>
	);
}




export default Login;

//hah 





