
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PIL import Image
import numpy
import sys
import math

rotacao = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

def controleSetas(key, x, y):
    if(key == GLUT_KEY_UP):
        glRotatef(-1.0, 1.0, 0.0, 0.0)
    elif(key == GLUT_KEY_DOWN):
        glRotatef(1.0, 1.0, 0.0, 0.0)
    elif(key == GLUT_KEY_LEFT):
        glRotatef(-1.0, 0.0, 1.0, 0.0)
    elif(key == GLUT_KEY_RIGHT):
        glRotatef(1.0, 0.0, 1.0, 0.0)

    glutPostRedisplay()

def desenharBonceDeNeve():
    glColor3f(1.0, 1.0, 1.0)

    # Corpo
    glTranslatef(0, 0.75, 0)
    glutSolidSphere(0.78, 20, 20)

    # Cabeca
    glTranslatef(0, 1, 0)
    glutSolidSphere(0.25, 20, 20)

    # Olhos
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslatef(0.05, 0.10, 0.18)
    glutSolidSphere(0.05, 10, 10)
    glTranslatef(-0.1, 0, 0)
    glutSolidSphere(0.05, 10, 10)
    glPopMatrix()

    # Nariz
    glColor3f(1, 0.5, 0.5)
    glutSolidCone(0.08, 0.5, 10, 2)

def display():

    # Cores e profundidades
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Chão invertido
    glPushMatrix()
    glRotate(180, 1, 0, 0)
    glBegin(GL_POLYGON)
    glColor3b(51, 51, 51)
    glNormal3f(0.0, -1.0, 0.0)
    glVertex3f(  5, 0.15, -5 )
    glVertex3f(  5, 0.15,  5 )
    glVertex3f( -5, 0.15,  5 )
    glVertex3f( -5, 0.15, -5 )
    glEnd()
    glPopMatrix()

    # Chão normal
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3b(51, 51, 51)
    glNormal3f(0.0, 1.0, 0.0)
    glVertex3f(  5, -0.15, -5 )
    glVertex3f(  5, -0.15,  5 )
    glVertex3f( -5, -0.15,  5 )
    glVertex3f( -5, -0.15, -5 )
    glEnd()
    glPopMatrix()

    glPushMatrix()

    glRotatef(rotacao[0], 0, 0, 1.0)

    desenharBonceDeNeve()

    glPopMatrix()

    glutSwapBuffers()

    return


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutCreateWindow('Boneco de Neve')

    # Sombreamento (suave)
    glShadeModel(GL_SMOOTH)

    # Face Culling (Corte de faces nao visualizadas)
    glEnable(GL_CULL_FACE)

    # Comparacoes de profundidade para atualizar o Buffer de profundidade
    glEnable(GL_DEPTH_TEST)

    # Renderizacao das cores com a iluminacao ativa
    glEnable(GL_COLOR_MATERIAL)

    # Habilita o foco de luz
    glEnable(GL_LIGHTING)

    # Posicionamento do foco da Luz
    lightZeroPosition = [1.0, 4.0, 15.0, 0.]

    # Cor da luz
    lightZeroColor = [0.8, 1.0, 0.8, 1.0]

    # Especifica a quantidade de focos e a posicao dela em coordenadas homogeneas
    glLightfv(GL_LIGHT1, GL_POSITION, lightZeroPosition)

    # Especificam a intensidade RGBA difusa da luz.
    glLightfv(GL_LIGHT1, GL_DIFFUSE, lightZeroColor)

    # Representa a atenuacao constante do foco
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 1.5)

    # Representa a atenuacao linear do foco
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05)

    # Habilita 1 foco de luz
    glEnable(GL_LIGHT1)

    # Habilita as funcoes das setas do teclado
    glutSpecialFunc(controleSetas)

    # Especifica a pilha de matriz de projecao como a pilha principal
    glMatrixMode(GL_PROJECTION)

    # Especifica o anlgulo de visao, proporcao de visao no eixo x, distancia de visao ate o proximo plano
    gluPerspective(40.0, 1.0, 1.0, 40.0)

    # Define o retorno de chamada da exibicao para a janela atual.
    glutDisplayFunc(display)

    # Cria uma matriz de visualizacao derivada de um ponto ocular, um ponto de referencia indicando o centro da cena e um vetor para cima.
    gluLookAt(0, 2, 5,
              0, 1, 0,
              0, 1, 0)

    glPushMatrix()

    glutMainLoop()

    return

if __name__ == '__main__':
    main()
