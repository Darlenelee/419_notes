# Report 2

> Requirements:
>
> Write a technical report about CPU, Memory, Storage(Ceph), Network and xPU  
> - Vendors or types or technologies
>   - Features
>   - Pros & Cons
> - Key indicators
>   - What, how to measure, scope
> - Your own comment
>   - For example
>     - How to tradeoff

## CPU

### Introduction

A **central processing unit (CPU)** is the electronic circuitry within a computer that carries out the instructions of a computer program by performing the basic arithmetic, logical, control and input/output (I/O) operations specified by the instructions. The computer industry has used the term "central processing unit" at least since the early 1960s. Traditionally, the term "CPU" refers to a processor, more specifically to its processing unit and control unit (CU), distinguishing these core elements of a computer from external components such as main memory and I/O circuitry.  

This report mainly includes Intel x86 and hardware virtualization.

### Moore's law

Moore's law is the observation that the number of transistors in a dense integrated circuit doubles about every two years. The observation is named after Gordon Moore, the co-founder of Fairchild Semiconductor and Intel, whose 1965 paper described a doubling every year in the number of components per integrated circuit, and projected this rate of growth would continue for at least another decade. In 1975, looking forward to the next decade, he revised the forecast to doubling every two years. The period is often quoted as 18 months because of a prediction by Intel executive David House (being a combination of the effect of more transistors and the transistors being faster).

### Intel

Intel Corporation (commonly known as Intel and stylized as intel) is an American multinational corporation and technology company headquartered in Santa Clara, California, in the Silicon Valley and on 6 Campus Drive, Parsippany-Troy Hills, New Jersey. It is the world's second largest and second highest valued semiconductor chip maker based on revenue after being overtaken by Samsung, and is the inventor of the x86 series of microprocessors, the processors found in most personal computers (PCs). Intel supplies processors for computer system manufacturers such as Apple, Lenovo, HP, and Dell. Intel also manufactures motherboard chipsets, network interface controllers and integrated circuits, flash memory, graphics chips, embedded processors and other devices related to communications and computing.

### x86

#### Overview

x86 is a family of backward-compatible instruction set architectures based on the Intel 8086 CPU and its Intel 8088 variant. The 8086 was introduced in 1978 as a fully 16-bit extension of Intel's 8-bit-based 8080 microprocessor, with memory segmentation as a solution for addressing more memory than can be covered by a plain 16-bit address. The term "x86" came into being because the names of several successors to Intel's 8086 processor end in "86", including the 80186, 80286, 80386 and 80486 processors.

![图片加载失败](https://upload.wikimedia.org/wikipedia/commons/2/23/Core_2_Duo_E6300.jpg)

#### Architecture

The x86 architecture is a variable instruction length, primarily "CISC" design with emphasis on backward compatibility. The instruction set is not typical CISC, however, but basically an extended version of the simple eight-bit 8008 and 8080 architectures. Byte-addressing is enabled and words are stored in memory with little-endian byte order. Memory access to unaligned addresses is allowed for all valid word sizes. The largest native size for integer arithmetic and memory addresses (or offsets) is 16, 32 or 64 bits depending on architecture generation (newer processors include direct support for smaller integers as well). Multiple scalar values can be handled simultaneously via the SIMD unit present in later generations, as described below. Immediate addressing offsets and immediate data may be expressed as 8-bit quantities for the frequently occurring cases or contexts where a -128..127 range is enough. Typical instructions are therefore 2 or 3 bytes in length (although some are much longer, and some are single-byte).

To further conserve encoding space, most registers are expressed in opcodes using three or four bits, the latter via an opcode prefix in 64-bit mode, while at most one operand to an instruction can be a memory location. However, this memory operand may also be the destination (or a combined source and destination), while the other operand, the source, can be either register or immediate. Among other factors, this contributes to a code size that rivals eight-bit machines and enables efficient use of instruction cache memory. The relatively small number of general registers (also inherited from its 8-bit ancestors) has made register-relative addressing (using small immediate offsets) an important method of accessing operands, especially on the stack. Much work has therefore been invested in making such accesses as fast as register accesses, i.e. a one cycle instruction throughput, in most circumstances where the accessed data is available in the top-level cache.

### Hardware Virtualization

#### Intel virtualization (VT-x)

Previously codenamed "Vanderpool", VT-x represents Intel's technology for virtualization on the x86 platform. On November 13, 2005, Intel released two models of Pentium 4 (Model 662 and 672) as the first Intel processors to support VT-x. The CPU flag for VT-x capability is "vmx"; in Linux, this can be checked via /proc/cpuinfo, or in macOS via sysctl machdep.cpu.features.

"vmx" stands for Virtual Machine Extensions, which adds ten new instructions: VMPTRLD, VMPTRST, VMCLEAR, VMREAD, VMWRITE, VMCALL, VMLAUNCH, VMRESUME, VMXOFF, and VMXON. These instructions permit entering and exiting a virtual execution mode where the guest OS perceives itself as running with full privilege (ring 0), but the host OS remains protected.

As of 2015, almost all newer server, desktop and mobile Intel processors support VT-x, with some of the Intel Atom processors as the primary exception. With some motherboards, users must enable Intel's VT-x feature in the BIOS setup before applications can make use of it.

Intel started to include Extended Page Tables (EPT), a technology for page-table virtualization, since the Nehalem architecture, released in 2008. In 2010, Westmere added support for launching the logical processor directly in real mode – a feature called "unrestricted guest", which requires EPT to work.

Since the Haswell microarchitecture (announced in 2013), Intel started to include VMCS shadowing as a technology that accelerates nested virtualization of VMMs. The virtual machine control structure (VMCS) is a data structure in memory that exists exactly once per VM, while it is managed by the VMM. With every change of the execution context between different VMs, the VMCS is restored for the current VM, defining the state of the VM's virtual processor. As soon as more than one VMM or nested VMMs are used, a problem appears in a way similar to what required shadow page table management to be invented, as described above. In such cases, VMCS needs to be shadowed multiple times (in case of nesting) and partially implemented in software in case there is no hardware support by the processor. To make shadow VMCS handling more efficient, Intel implemented hardware support for VMCS shadowing.

### Comment

- Nowadays Moore's Law is expired and CPU's development become smooth. The important problem is how to make the best use of existing resources.
- Hence, I think Hardware Virtualization is one of the ways to gather and alloc resources.



