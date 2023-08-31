import './bloc1.css'


const Bloc1 = () => {
    return (
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
    );

}

export default Bloc1