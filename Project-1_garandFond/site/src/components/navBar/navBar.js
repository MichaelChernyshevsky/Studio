import NavigationBar_ButtonBuilder from "./navBar_buttonBuilder";
import temp_logotype from '../../assets/temp/logotype.svg'

import * as constants from "../../constants/navBar_text";


const NavigationBar = () => {
    return (
        <nav className="navigation_bar">
            <img src={temp_logotype} />
            <text>{constants.NAVBAR_TITLE}</text>
            <NavigationBar_ButtonBuilder/>
        </nav>
    );
}

export default NavigationBar;


