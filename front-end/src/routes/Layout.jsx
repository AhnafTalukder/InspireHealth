import { Outlet, Link } from "react-router-dom";
import './Layout.css'
import Logo from '../assets/logo.png'

const Layout = () => {
  return (
    <div>
      <div className="nav-bar">
        <div className="logo">
            <img width="20%" src={Logo} alt="" />
        </div>
        <ul>
          <li className="underline home-link" key="home-button">
            <Link to="/">
              Home
            </Link>
          </li>
          <li className="underline discover-link" key="discover-button">
            <Link to="/discover">
              Discover
            </Link>
          </li>
          <li className="underline about-link" key="about-button">
            <Link to="/about-us">
              About Us
            </Link>
          </li>
          <li className="underline network-link" key="network-button">
            <Link to="/join-our-network">
              Join Network
            </Link>
          </li>
          <li className="underline contact-link" key="contact-button">
            <Link to="/contact-us">
              Contact Us
            </Link>
          </li>
        </ul>
      </div>
      <Outlet />
    </div>
  );
};

export default Layout;