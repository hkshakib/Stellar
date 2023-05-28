import React from 'react';
import Navbar from "../Components/Navbar";
const Layout = (props) => (
    <div>
        <Navbar/>
        {props.children}
    </div>
);

export default Layout;