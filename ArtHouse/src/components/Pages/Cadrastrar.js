import React, {Component} from 'react';
import {StyleSheet, View, Image, ScrollView, Text, Alert, Button, TextInput} from 'react-native';
import firebase from 'react-native-firebase';



export default class Cadrastrar extends Component {
    constructor(props) {
    super(props);
    this.state = {
            InputEmail: '',
            InputPass: '',
        }
    }

    async SalvarCadastro() {
      const { InputEmail, InputPass } = this.state;

      if ((InputEmail == '') || (InputPass == '') || (InputEmail == '' && InputPass == '')) {
          Alert.alert('Prencha os campos para concluir o cadastro');
      }
      else if (InputPass.length < 8) {
          Alert.alert('Senha precisa ter ao menos 8 caracteres')
      }
      else if (InputEmail != '' && InputPass != '') {
        try {
          await firebase.auth().createUserWithEmailAndPassword(InputEmail, InputPass)
          Alert.alert('Cadastro Realizado com Sucesso');
          this.props.navigation.navigate('Tela3')
      }
          catch(err){
            Alert.alert('Email/Senha não forão inseridos corretamente!');  
    } 

  }
}



  render() {
    return (

      <View style={styles.container}>
      <View>
      <Image style={styles.image0} source={require('../images/arthouselogo.jpg')}/>
        <Text style={styles.fonte}>          Cadastro </Text>
      </View>
      <View style={styles.form}>
        <TextInput style = {styles.input}
          placeholder='Insira seu E-mail: '
          autoCapitalize="none"
          onChangeText={(InputEmail) => this.setState({ InputEmail })}
        />
        <TextInput style = {styles.input}
          placeholder='Insira sua senha: '
          autoCapitalize="none"
          secureTextEntry
          onChangeText={(InputPass) => this.setState({ InputPass })}
        />
      </View>
      <View>
        <Button title = "Criar Conta" onPress={() => this.SalvarCadastro()}/>
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
    fontSize: 30,
    color: 'black',

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
Cadrastrar.navigationOptions = {
    header: null,
};

