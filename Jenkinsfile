pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/HeetVasani1/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Divsion.py"
                sh "./Divsion.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
                sh "chmod u+x Test1.py"
                sh "./Test1.py"
                sh "chmod u+x Test2.py"
                sh "./Test2.py"
                sh "chmod u+x Tes3t.py"
                sh "./Test3.py"
                sh "chmod u+x Test4.py"
                sh "./Test4.py"
                
            }
        }
    } 
}
