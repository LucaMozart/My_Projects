import React, {Component} from 'react';
import {StyleSheet, View, Image, ScrollView, Text, Alert, Button, TextInput} from 'react-native';
import firebase from 'react-native-firebase';



export default class Login extends Component {
    constructor(props) {
    super(props);
    this.state = {
            inputEmail: 'default',
            inputPass: 'default',
        };
    };

  validarLogin = async () => {

    const {inputEmail, inputPass } = this.state;
    if ((this.state.inputEmail == '' && this.state.inputPass == "") || (this.state.inputEmail == '' || this.state.inputPass == "")) {
      Alert.alert('Insira usuário e/ou senha.');
    }

    else {
      try {
        await firebase.auth().signInWithEmailAndPassword(this.state.inputEmail,this.state.inputPass);
        this.props.navigation.navigate('Tela1')
      }
            catch(err){
                Alert.alert('Usuario ou senha invalidos.');  
            } 
    }
    }



  render() {
    return (

      <View style={styles.container}>
      <View>
      <Image style={styles.image0} source={require('../images/arthouselogo.jpg')}/>
        <Text style={styles.fonte}>         Login121312 </Text>
      </View>
      <View style={styles.form}>
        <TextInput style = {styles.input}
          placeholder='Insira seu E-mail: '
          autoCapitalize="none"
          onChangeText={inputEmail => this.setState({ inputEmail })}
        />
        <TextInput style = {styles.input}
          placeholder='Insira sua senha: '
          autoCapitalize="none"
          secureTextEntry
          onChangeText={inputPass => this.setState({ inputPass })}
        />
      </View>
      <View>
        <Button title = "Logar"  onPress={this.validarLogin}/>
        <Text style={styles.fonte2} onPress={() => this.props.navigation.navigate('Tela9')}>Criar conta</Text>
      </View>

      </View>
    );
  }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#FCFFFA',
    },
      fonte:{
    fontSize: 40,
    color: 'black',
  },
        fonte2:{
    fontSize: 30,

  },

    form: {
        padding: 20
    },
    input: {
        height: 60,
        width: 300,
        borderRadius: 10,
        margin: 10,
        backgroundColor: '#FFDA2E',
        color: '#000'
    },
    image: {
      width: 200,
      height: 200,
    },
    text: {
      color: '#fff',
      textAlign: 'center',
      fontWeight: '700',
      fontSize: 15,
      marginTop: -5

    },
      image0: {
    width:  300, 
    height: 102,
  },




});
Login.navigationOptions = {
    header: null,
};

