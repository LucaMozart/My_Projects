import React, {Component} from 'react';
import {createStackNavigator,createAppContainer} from 'react-navigation';

import Start from './Start';
import Menu from './Menu';
import Login from './Login';
import Papel from './Papel';
import Produto from './Produto';
import Wellcome from './Wellcome';
import Painel from './Painel';
import Cadrastrar from './Cadrastrar';





const MainNavigator = createStackNavigator({

  Tela1: {screen: Start},
  Tela2: {screen: Menu},
  Tela3: {screen: Login},
  Tela4: {screen: Papel},
  Tela5: {screen: Produto},
  Tela7: {screen: Wellcome},
  Tela8: {screen: Painel},
  Tela9: {screen: Cadrastrar}



},
{
  initialRouteName:'Tela3'
});

const AppContainer =  createAppContainer(MainNavigator);

export default class App extends Component{
  render() {
    return <AppContainer/>;
      
  }
}
