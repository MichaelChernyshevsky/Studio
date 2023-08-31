
// import Bloc1 from '../components/body/bloc1';
import img_phone from '../assets/navBar/phone.svg'
import img_mail from '../assets/navBar/mail.svg'
import img_person from '../assets/navBar/person.svg'
import img_menu from '../assets/navBar/menu.svg'
import temp_logotype from '../assets/temp/logotype.svg'

import 'bootstrap'


function MainPage() {
  return (
    <div>
      <nav className="navigation_bar">

        <div className="info" >
          <img className="logo" src={temp_logotype} />
          <text className='title'>Оформление банковской гарантии</text>
        </div>
        <div className='placeholder'>
          <img className='button' src={img_phone} />
          <img className='button' src={img_mail} />
          <img className='button' src={img_person} />
          <img className='button' src={img_menu} />
        </div>
      </nav>



      <body>
      <div className="bloc1">
            <div className='column-bloc1'>
                <text className='warning-bloc1'>Мы не предоставляем кредитование для физических лиц </text>
                <text className='title-bloc1'> Получение банковской гаранти <p/>по всей России за 3 часа онлайн<p/>для ИП и Юридических лиц</text>
                <text className='free-bloc1'>С бесплатным оформлением!</text>
                <div className='form-bloc1'>
                    <input type='phone' className='input-bloc1' placeholder='+7 (999) 999-99-99'>
                    </input>
                    <button className='button-bloc1'>
                        Получить гарантию
                    </button>
                </div>
                <div className='list'>

                </div>
            </div>
        </div>
      </body>

    </div>
  );
}

export default MainPage;
