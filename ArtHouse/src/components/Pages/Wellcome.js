import React, {Component} from 'react';
import { View, Text, TextInput, Button, Image,TouchableOpacity,TouchableHighlight } from 'react-native';
export default class Wellcome extends Component {
  render() {
   return (
       <View>
          <View style={{flex: 1, paddingTop:100, justifyContent: 'center', alignItems: 'center' }}>
            <Image style= {{ width: 300, height:102}} source={require('../images/arthouselogo.jpg')}/>
          </View>
          <View style={{flex: 1, paddingTop:100, justifyContent: 'center', alignItems: 'center' }}>
            <Text style={{ fontSize: 30, color: 'black' }}>Seja Bem-Vindo!</Text>
           </View>
             <View style={{flex: 3, justifyContent:'center', flexDirection:'column', alignItems: 'center', paddingTop:160}}>
               <TouchableOpacity style={{height: 35, width: 100, backgroundColor: 'gray', borderColor: 'black', borderWidth:0.5, margin:10}}  onPress={() => this.props.navigation.navigate('Tela3')}>
                   <Text style={{color: 'white', textAlign: 'center', fontSize: 20}}> Acessar </Text>
               </TouchableOpacity>
               <TouchableOpacity style={{height: 35, width: 110, backgroundColor: 'gray', borderColor: 'black', borderWidth:0.5}} onPress={() => this.props.navigation.navigate('Tela6')}>
                   <Text style={{color: 'white', textAlign: 'center', fontSize: 20}}> Cadastrar </Text>
               </TouchableOpacity>
             </View>
       </View>
     
   )
  }    
};
Wellcome.navigationOptions = {
  header: null,
};
