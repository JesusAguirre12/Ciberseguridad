
sw-05:     formato del fichero elf64-x86-64


Desensamblado de la sección .init:

0000000000001000 <_init>:
    1000:	48 83 ec 08          	sub    $0x8,%rsp
    1004:	48 8b 05 dd 2f 00 00 	mov    0x2fdd(%rip),%rax        # 3fe8 <__gmon_start__>
    100b:	48 85 c0             	test   %rax,%rax
    100e:	74 02                	je     1012 <_init+0x12>
    1010:	ff d0                	call   *%rax
    1012:	48 83 c4 08          	add    $0x8,%rsp
    1016:	c3                   	ret

Desensamblado de la sección .plt:

0000000000001020 <.plt>:
    1020:	ff 35 e2 2f 00 00    	push   0x2fe2(%rip)        # 4008 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:	ff 25 e4 2f 00 00    	jmp    *0x2fe4(%rip)        # 4010 <_GLOBAL_OFFSET_TABLE_+0x10>
    102c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000001030 <puts@plt>:
    1030:	ff 25 e2 2f 00 00    	jmp    *0x2fe2(%rip)        # 4018 <puts@GLIBC_2.2.5>
    1036:	68 00 00 00 00       	push   $0x0
    103b:	e9 e0 ff ff ff       	jmp    1020 <.plt>

0000000000001040 <strlen@plt>:
    1040:	ff 25 da 2f 00 00    	jmp    *0x2fda(%rip)        # 4020 <strlen@GLIBC_2.2.5>
    1046:	68 01 00 00 00       	push   $0x1
    104b:	e9 d0 ff ff ff       	jmp    1020 <.plt>

0000000000001050 <__stack_chk_fail@plt>:
    1050:	ff 25 d2 2f 00 00    	jmp    *0x2fd2(%rip)        # 4028 <__stack_chk_fail@GLIBC_2.4>
    1056:	68 02 00 00 00       	push   $0x2
    105b:	e9 c0 ff ff ff       	jmp    1020 <.plt>

0000000000001060 <printf@plt>:
    1060:	ff 25 ca 2f 00 00    	jmp    *0x2fca(%rip)        # 4030 <printf@GLIBC_2.2.5>
    1066:	68 03 00 00 00       	push   $0x3
    106b:	e9 b0 ff ff ff       	jmp    1020 <.plt>

0000000000001070 <memset@plt>:
    1070:	ff 25 c2 2f 00 00    	jmp    *0x2fc2(%rip)        # 4038 <memset@GLIBC_2.2.5>
    1076:	68 04 00 00 00       	push   $0x4
    107b:	e9 a0 ff ff ff       	jmp    1020 <.plt>

0000000000001080 <fgets@plt>:
    1080:	ff 25 ba 2f 00 00    	jmp    *0x2fba(%rip)        # 4040 <fgets@GLIBC_2.2.5>
    1086:	68 05 00 00 00       	push   $0x5
    108b:	e9 90 ff ff ff       	jmp    1020 <.plt>

Desensamblado de la sección .plt.got:

0000000000001090 <__cxa_finalize@plt>:
    1090:	ff 25 62 2f 00 00    	jmp    *0x2f62(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    1096:	66 90                	xchg   %ax,%ax

Desensamblado de la sección .text:

00000000000010a0 <_start>:
    10a0:	31 ed                	xor    %ebp,%ebp
    10a2:	49 89 d1             	mov    %rdx,%r9
    10a5:	5e                   	pop    %rsi
    10a6:	48 89 e2             	mov    %rsp,%rdx
    10a9:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
    10ad:	50                   	push   %rax
    10ae:	54                   	push   %rsp
    10af:	4c 8d 05 fa 02 00 00 	lea    0x2fa(%rip),%r8        # 13b0 <__libc_csu_fini>
    10b6:	48 8d 0d 93 02 00 00 	lea    0x293(%rip),%rcx        # 1350 <__libc_csu_init>
    10bd:	48 8d 3d 28 01 00 00 	lea    0x128(%rip),%rdi        # 11ec <main>
    10c4:	ff 15 16 2f 00 00    	call   *0x2f16(%rip)        # 3fe0 <__libc_start_main@GLIBC_2.2.5>
    10ca:	f4                   	hlt
    10cb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000010d0 <deregister_tm_clones>:
    10d0:	48 8d 3d 81 2f 00 00 	lea    0x2f81(%rip),%rdi        # 4058 <__TMC_END__>
    10d7:	48 8d 05 7a 2f 00 00 	lea    0x2f7a(%rip),%rax        # 4058 <__TMC_END__>
    10de:	48 39 f8             	cmp    %rdi,%rax
    10e1:	74 15                	je     10f8 <deregister_tm_clones+0x28>
    10e3:	48 8b 05 ee 2e 00 00 	mov    0x2eee(%rip),%rax        # 3fd8 <_ITM_deregisterTMCloneTable>
    10ea:	48 85 c0             	test   %rax,%rax
    10ed:	74 09                	je     10f8 <deregister_tm_clones+0x28>
    10ef:	ff e0                	jmp    *%rax
    10f1:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    10f8:	c3                   	ret
    10f9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001100 <register_tm_clones>:
    1100:	48 8d 3d 51 2f 00 00 	lea    0x2f51(%rip),%rdi        # 4058 <__TMC_END__>
    1107:	48 8d 35 4a 2f 00 00 	lea    0x2f4a(%rip),%rsi        # 4058 <__TMC_END__>
    110e:	48 29 fe             	sub    %rdi,%rsi
    1111:	48 89 f0             	mov    %rsi,%rax
    1114:	48 c1 ee 3f          	shr    $0x3f,%rsi
    1118:	48 c1 f8 03          	sar    $0x3,%rax
    111c:	48 01 c6             	add    %rax,%rsi
    111f:	48 d1 fe             	sar    $1,%rsi
    1122:	74 14                	je     1138 <register_tm_clones+0x38>
    1124:	48 8b 05 c5 2e 00 00 	mov    0x2ec5(%rip),%rax        # 3ff0 <_ITM_registerTMCloneTable>
    112b:	48 85 c0             	test   %rax,%rax
    112e:	74 08                	je     1138 <register_tm_clones+0x38>
    1130:	ff e0                	jmp    *%rax
    1132:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    1138:	c3                   	ret
    1139:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001140 <__do_global_dtors_aux>:
    1140:	80 3d 21 2f 00 00 00 	cmpb   $0x0,0x2f21(%rip)        # 4068 <completed.0>
    1147:	75 2f                	jne    1178 <__do_global_dtors_aux+0x38>
    1149:	55                   	push   %rbp
    114a:	48 83 3d a6 2e 00 00 	cmpq   $0x0,0x2ea6(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    1151:	00 
    1152:	48 89 e5             	mov    %rsp,%rbp
    1155:	74 0c                	je     1163 <__do_global_dtors_aux+0x23>
    1157:	48 8b 3d f2 2e 00 00 	mov    0x2ef2(%rip),%rdi        # 4050 <__dso_handle>
    115e:	e8 2d ff ff ff       	call   1090 <__cxa_finalize@plt>
    1163:	e8 68 ff ff ff       	call   10d0 <deregister_tm_clones>
    1168:	c6 05 f9 2e 00 00 01 	movb   $0x1,0x2ef9(%rip)        # 4068 <completed.0>
    116f:	5d                   	pop    %rbp
    1170:	c3                   	ret
    1171:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    1178:	c3                   	ret
    1179:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001180 <frame_dummy>:
    1180:	e9 7b ff ff ff       	jmp    1100 <register_tm_clones>

0000000000001185 <strcmp>:
    1185:	55                   	push   %rbp
    1186:	48 89 e5             	mov    %rsp,%rbp
    1189:	48 89 7d d8          	mov    %rdi,-0x28(%rbp)
    118d:	48 89 75 d0          	mov    %rsi,-0x30(%rbp)
    1191:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    1195:	48 89 45 f0          	mov    %rax,-0x10(%rbp)
    1199:	48 8b 45 d0          	mov    -0x30(%rbp),%rax
    119d:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    11a1:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
    11a5:	48 8d 50 01          	lea    0x1(%rax),%rdx
    11a9:	48 89 55 f0          	mov    %rdx,-0x10(%rbp)
    11ad:	0f b6 00             	movzbl (%rax),%eax
    11b0:	88 45 ee             	mov    %al,-0x12(%rbp)
    11b3:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    11b7:	48 8d 50 01          	lea    0x1(%rax),%rdx
    11bb:	48 89 55 f8          	mov    %rdx,-0x8(%rbp)
    11bf:	0f b6 00             	movzbl (%rax),%eax
    11c2:	88 45 ef             	mov    %al,-0x11(%rbp)
    11c5:	80 7d ee 00          	cmpb   $0x0,-0x12(%rbp)
    11c9:	75 0c                	jne    11d7 <strcmp+0x52>
    11cb:	0f b6 45 ee          	movzbl -0x12(%rbp),%eax
    11cf:	0f b6 55 ef          	movzbl -0x11(%rbp),%edx
    11d3:	29 d0                	sub    %edx,%eax
    11d5:	eb 13                	jmp    11ea <strcmp+0x65>
    11d7:	0f b6 45 ee          	movzbl -0x12(%rbp),%eax
    11db:	3a 45 ef             	cmp    -0x11(%rbp),%al
    11de:	74 c1                	je     11a1 <strcmp+0x1c>
    11e0:	0f b6 45 ee          	movzbl -0x12(%rbp),%eax
    11e4:	0f b6 55 ef          	movzbl -0x11(%rbp),%edx
    11e8:	29 d0                	sub    %edx,%eax
    11ea:	5d                   	pop    %rbp
    11eb:	c3                   	ret

00000000000011ec <main>:
    11ec:	55                   	push   %rbp
    11ed:	48 89 e5             	mov    %rsp,%rbp
    11f0:	48 81 ec 20 02 00 00 	sub    $0x220,%rsp
    11f7:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    11fe:	00 00 
    1200:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1204:	31 c0                	xor    %eax,%eax
    1206:	48 8d 85 f0 fd ff ff 	lea    -0x210(%rbp),%rax
    120d:	ba 00 01 00 00       	mov    $0x100,%edx
    1212:	be 00 00 00 00       	mov    $0x0,%esi
    1217:	48 89 c7             	mov    %rax,%rdi
    121a:	e8 51 fe ff ff       	call   1070 <memset@plt>
    121f:	48 8d 85 f0 fe ff ff 	lea    -0x110(%rbp),%rax
    1226:	ba 00 01 00 00       	mov    $0x100,%edx
    122b:	be 00 00 00 00       	mov    $0x0,%esi
    1230:	48 89 c7             	mov    %rax,%rdi
    1233:	e8 38 fe ff ff       	call   1070 <memset@plt>
    1238:	48 8d 3d ed 0d 00 00 	lea    0xded(%rip),%rdi        # 202c <flag+0x1c>
    123f:	b8 00 00 00 00       	mov    $0x0,%eax
    1244:	e8 17 fe ff ff       	call   1060 <printf@plt>
    1249:	48 8b 15 10 2e 00 00 	mov    0x2e10(%rip),%rdx        # 4060 <stdin@GLIBC_2.2.5>
    1250:	48 8d 85 f0 fd ff ff 	lea    -0x210(%rbp),%rax
    1257:	be 00 01 00 00       	mov    $0x100,%esi
    125c:	48 89 c7             	mov    %rax,%rdi
    125f:	e8 1c fe ff ff       	call   1080 <fgets@plt>
    1264:	48 8d 85 f0 fd ff ff 	lea    -0x210(%rbp),%rax
    126b:	48 89 c7             	mov    %rax,%rdi
    126e:	e8 cd fd ff ff       	call   1040 <strlen@plt>
    1273:	48 89 85 e8 fd ff ff 	mov    %rax,-0x218(%rbp)
    127a:	48 83 bd e8 fd ff ff 	cmpq   $0x0,-0x218(%rbp)
    1281:	00 
    1282:	0f 84 8f 00 00 00    	je     1317 <main+0x12b>
    1288:	48 8b 85 e8 fd ff ff 	mov    -0x218(%rbp),%rax
    128f:	48 83 e8 01          	sub    $0x1,%rax
    1293:	0f b6 84 05 f0 fd ff 	movzbl -0x210(%rbp,%rax,1),%eax
    129a:	ff 
    129b:	3c 0a                	cmp    $0xa,%al
    129d:	75 13                	jne    12b2 <main+0xc6>
    129f:	48 8b 85 e8 fd ff ff 	mov    -0x218(%rbp),%rax
    12a6:	48 83 e8 01          	sub    $0x1,%rax
    12aa:	c6 84 05 f0 fd ff ff 	movb   $0x0,-0x210(%rbp,%rax,1)
    12b1:	00 
    12b2:	48 c7 85 e0 fd ff ff 	movq   $0x0,-0x220(%rbp)
    12b9:	00 00 00 00 
    12bd:	eb 31                	jmp    12f0 <main+0x104>
    12bf:	48 8b 85 e0 fd ff ff 	mov    -0x220(%rbp),%rax
    12c6:	48 8d 14 00          	lea    (%rax,%rax,1),%rdx
    12ca:	48 8d 05 3f 0d 00 00 	lea    0xd3f(%rip),%rax        # 2010 <flag>
    12d1:	0f b6 04 02          	movzbl (%rdx,%rax,1),%eax
    12d5:	48 8d 8d f0 fe ff ff 	lea    -0x110(%rbp),%rcx
    12dc:	48 8b 95 e0 fd ff ff 	mov    -0x220(%rbp),%rdx
    12e3:	48 01 ca             	add    %rcx,%rdx
    12e6:	88 02                	mov    %al,(%rdx)
    12e8:	48 83 85 e0 fd ff ff 	addq   $0x1,-0x220(%rbp)
    12ef:	01 
    12f0:	48 83 bd e0 fd ff ff 	cmpq   $0xd,-0x220(%rbp)
    12f7:	0d 
    12f8:	76 c5                	jbe    12bf <main+0xd3>
    12fa:	48 8d 95 f0 fe ff ff 	lea    -0x110(%rbp),%rdx
    1301:	48 8d 85 f0 fd ff ff 	lea    -0x210(%rbp),%rax
    1308:	48 89 d6             	mov    %rdx,%rsi
    130b:	48 89 c7             	mov    %rax,%rdi
    130e:	e8 72 fe ff ff       	call   1185 <strcmp>
    1313:	85 c0                	test   %eax,%eax
    1315:	74 11                	je     1328 <main+0x13c>
    1317:	48 8d 3d 27 0d 00 00 	lea    0xd27(%rip),%rdi        # 2045 <flag+0x35>
    131e:	e8 0d fd ff ff       	call   1030 <puts@plt>
    1323:	e9 10 ff ff ff       	jmp    1238 <main+0x4c>
    1328:	90                   	nop
    1329:	48 8d 3d 31 0d 00 00 	lea    0xd31(%rip),%rdi        # 2061 <flag+0x51>
    1330:	e8 fb fc ff ff       	call   1030 <puts@plt>
    1335:	b8 00 00 00 00       	mov    $0x0,%eax
    133a:	48 8b 4d f8          	mov    -0x8(%rbp),%rcx
    133e:	64 48 2b 0c 25 28 00 	sub    %fs:0x28,%rcx
    1345:	00 00 
    1347:	74 05                	je     134e <main+0x162>
    1349:	e8 02 fd ff ff       	call   1050 <__stack_chk_fail@plt>
    134e:	c9                   	leave
    134f:	c3                   	ret

0000000000001350 <__libc_csu_init>:
    1350:	41 57                	push   %r15
    1352:	4c 8d 3d 8f 2a 00 00 	lea    0x2a8f(%rip),%r15        # 3de8 <__frame_dummy_init_array_entry>
    1359:	41 56                	push   %r14
    135b:	49 89 d6             	mov    %rdx,%r14
    135e:	41 55                	push   %r13
    1360:	49 89 f5             	mov    %rsi,%r13
    1363:	41 54                	push   %r12
    1365:	41 89 fc             	mov    %edi,%r12d
    1368:	55                   	push   %rbp
    1369:	48 8d 2d 80 2a 00 00 	lea    0x2a80(%rip),%rbp        # 3df0 <__do_global_dtors_aux_fini_array_entry>
    1370:	53                   	push   %rbx
    1371:	4c 29 fd             	sub    %r15,%rbp
    1374:	48 83 ec 08          	sub    $0x8,%rsp
    1378:	e8 83 fc ff ff       	call   1000 <_init>
    137d:	48 c1 fd 03          	sar    $0x3,%rbp
    1381:	74 1b                	je     139e <__libc_csu_init+0x4e>
    1383:	31 db                	xor    %ebx,%ebx
    1385:	0f 1f 00             	nopl   (%rax)
    1388:	4c 89 f2             	mov    %r14,%rdx
    138b:	4c 89 ee             	mov    %r13,%rsi
    138e:	44 89 e7             	mov    %r12d,%edi
    1391:	41 ff 14 df          	call   *(%r15,%rbx,8)
    1395:	48 83 c3 01          	add    $0x1,%rbx
    1399:	48 39 dd             	cmp    %rbx,%rbp
    139c:	75 ea                	jne    1388 <__libc_csu_init+0x38>
    139e:	48 83 c4 08          	add    $0x8,%rsp
    13a2:	5b                   	pop    %rbx
    13a3:	5d                   	pop    %rbp
    13a4:	41 5c                	pop    %r12
    13a6:	41 5d                	pop    %r13
    13a8:	41 5e                	pop    %r14
    13aa:	41 5f                	pop    %r15
    13ac:	c3                   	ret
    13ad:	0f 1f 00             	nopl   (%rax)

00000000000013b0 <__libc_csu_fini>:
    13b0:	c3                   	ret

Desensamblado de la sección .fini:

00000000000013b4 <_fini>:
    13b4:	48 83 ec 08          	sub    $0x8,%rsp
    13b8:	48 83 c4 08          	add    $0x8,%rsp
    13bc:	c3                   	ret
