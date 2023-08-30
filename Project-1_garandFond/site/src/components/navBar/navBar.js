import temp_logotype from '../../assets/temp/logotype.svg'
import "./style.css"
import img_phone from '../../assets/navBar/phone.svg'
import img_mail from '../../assets/navBar/mail.svg'
import img_person from '../../assets/navBar/person.svg'
import img_menu from '../../assets/navBar/menu.svg'
import * as constants from "../../constants/site/nav/navBar_text";


const NavigationBar = () => {
    return (
        <nav className="navigation_bar">

            <span className="info" >
                <img className="logo" src={temp_logotype} />
                <text className='title'>{constants.NAVBAR_TITLE}</text>
            </span>
            <span>
                <img className='button' src={img_phone} />
                <img className='button' src={img_mail} />
                <img className='button' src={img_person} />
                <img className='button' src={img_menu} />
            </span>
            

        </nav>
    );
}

export default NavigationBar;


