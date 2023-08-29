import img_phone from '../../assets/navBar/phone.svg'
import img_mail from  '../../assets/navBar/mail.svg'
import img_person from '../../assets/navBar/person.svg'
import img_menu from '../../assets/navBar/menu.svg'

const NavigationBar_ButtonBuilder = () => {
    return ( 
        <div className='NavBar-buttons'>
            <img src={img_phone} />
            <img src={img_mail}/>
            <img src={img_person}/>
            <img src={img_menu}/>
        </div>
     );
}
 
export default NavigationBar_ButtonBuilder;